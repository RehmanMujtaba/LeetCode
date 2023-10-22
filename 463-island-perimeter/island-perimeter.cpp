class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {

        // Initialize Perimeter to 0
        int p = 0;

        // Loop though the grid
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {


                // if (p == 0) cout << "Grid Size is: " << grid.size() << "x" << grid[i].size() << '\n';

                // Land tile
                if (grid[i][j] == 1) {
                    
                    // Top and Bottom edge
                    if(i == 0) {
                        p += 1;
                    }

                    if ( i == grid.size() - 1) {
                        p += 1;
                    }

                    // Left and Right edge
                    if(j == 0 ) {
                        p += 1;
                    }

                    if ( j == grid[i].size() - 1) {
                        p += 1;
                    
                        // cout << "Right Edge Touching Boundry, +1 Permiter \n"; 
                    }

                    // Left Edge Water?
                    if (i - 1 >= 0 && grid[i-1][j] == 0) {
                        p += 1;
                    }

                    // Right Edge Water?
                    if (i + 1 < grid.size() && grid[i+1][j] == 0) {
                        p += 1;
                    }

                    if (j - 1 >= 0 && grid[i][j-1] == 0) {
                        p += 1;
                    }

                    if (j + 1 < grid[i].size() && grid[i][j+1] == 0) {
                        p += 1;
                    }
                }
            }
        }

        return p;
    }
};