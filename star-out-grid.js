function starOutGrid(grid) {
    for (let i = 0; i < grid.length; i++){
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] != star) {
                if (grid[i - 1] != undefined && grid[i - 1][j] === star) {
                    grid[i][j] = star;
                }
                if (grid[i][j - 1] != undefined && grid[i][j - 1] === star) {
                    grid[i][j] = star;
                }
            }
        }
    }
    return grid
}