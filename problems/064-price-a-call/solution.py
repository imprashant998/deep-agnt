KINDS = (("input_tokens", "input"), ("output_tokens", "output"),
         ("cache_read_tokens", "cache_read"), ("cache_write_tokens", "cache_write"))
MILLION = 10**6

def _raw(usage, price):
    """Exact cost, still multiplied by 1e6 (no division yet)."""
    return sum(usage.get(u, 0) * price[p] for u, p in KINDS)

def _ceil_div(n, d):
    return -(-n // d)

def call_cost(usage, price):
    return _ceil_div(_raw(usage, price), MILLION)

def cost_report(calls, prices):
    raw_by_model = {}
    unknown = set()
    for call in calls:
        model = call["model"]
        if model not in prices:
            unknown.add(model)
            continue
        raw_by_model[model] = raw_by_model.get(model, 0) + _raw(call["usage"], prices[model])
    return {
        "by_model": {m: _ceil_div(r, MILLION) for m, r in raw_by_model.items()},
        "total": _ceil_div(sum(raw_by_model.values()), MILLION),
        "unknown": sorted(unknown),
    }


