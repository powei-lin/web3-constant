def _load_json(file_path):
    import json
    import pkg_resources

    ifile = pkg_resources.resource_stream(__name__, file_path)
    d = json.load(ifile)
    return d


BALANCER_V2_VAULT_ABI = _load_json("json/Vault.json")
BALANCER_V2_WEIGHTED_POOL_ABI = _load_json("json/WeightedPool.json")
BALANCER_V2_WEIGHTED_POOL_2TOKENS_ABI = _load_json("json/WeightedPool2Tokens.json")

BEETHOVENX_VAULT_ABI = BALANCER_V2_VAULT_ABI
BEETHOVENX_WEIGHTED_POOL_ABI = BALANCER_V2_WEIGHTED_POOL_ABI
BEETHOVENX_WEIGHTED_POOL_2TOKENS_ABI = BALANCER_V2_WEIGHTED_POOL_2TOKENS_ABI
