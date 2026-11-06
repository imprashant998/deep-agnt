import math


def next_token_probs(logits, temperature=1.0, top_p=1.0):
    """Turn logits into probabilities, applying temperature and top-p."""
    max_logit = max(logits)
    shifted_logits = [l-max_logit for l in logits]
    if temperature == 0:
        # return the token with max logit
        max_index = logits.index(max_logit)
        probs = [0.0 for _ in range(len(logits))]
        probs[max_index] = 1.0
        return probs
    else:
        exp_shifted_logits = [math.exp(l/temperature) for l in shifted_logits ]
        sum_exp = sum(exp_shifted_logits)
        probs = [l/sum_exp for l in exp_shifted_logits]
        # now be need to sort the probs and keep track of their index
        tokens_probs_map = {i:probs[i] for i in range(len(probs))}
        tokens_probs_map = dict(sorted(tokens_probs_map.items() ,key = lambda x:x[1],reverse = True))
        output_tokens_probs_map = {}
        cummulative_probs = 0
        for index,prob in tokens_probs_map.items():
            output_tokens_probs_map[index] = prob
            cummulative_probs += prob
            if cummulative_probs >= top_p:
                break
        output = [0 for _ in range(len(logits))]
        for index,prob in output_tokens_probs_map.items():
            output[index] = prob
        # scale output to make sum = 1
        sum_output = sum(output)
        return [prob/sum_output for prob in output]


def sample(probs, u):
    """The index chosen by a uniform number u in [0, 1)."""
    running_sum_probs = []
    running_sum = 0
    for p in probs:
        running_sum += p
        running_sum_probs.append(running_sum)
    for i in range(len(running_sum_probs)):
        if running_sum_probs[i] > u:
            return i
