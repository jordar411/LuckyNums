function snakeToCamel(str) {
    return str.replace(/(?<!_)_(?!_)([a-zA-Z])/g, g => g[1].toUpperCase())
}