def _load_json(file_path):
    import json
    import pkg_resources

    ifile = pkg_resources.resource_stream(__name__, file_path)
    d = json.load(ifile)
    return d


UNISWAP_V2_PAIR_ABI = _load_json("json/UniswapV2Pair.json")
UNISWAP_V2_ROUTER_ABI = _load_json("json/UniswapV2Router.json")
UNISWAP_V2_FACTORY_ABI = _load_json("json/UniswapV2Factory.json")

SPOOKY_SWAP_ROUTER_ABI = UNISWAP_V2_ROUTER_ABI
SPOOKY_SWAP_FACTORY_ABI = UNISWAP_V2_FACTORY_ABI
SPOOKY_SWAP_PAIR_ABI = UNISWAP_V2_PAIR_ABI
