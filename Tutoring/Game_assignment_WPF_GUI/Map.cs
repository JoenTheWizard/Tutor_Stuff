using System.Collections.Generic;

namespace Game_Assignment
{
    public class Map : Game
    {
        //Make a list of covers and obstacles
        public List<Cover> covers;
        public List<Obstacle> obstacles;
        //This will be the map object
        public Map() {
            //Initialize the list of obstacles and covers list
            covers = new List<Cover>();
            obstacles = new List<Obstacle>();
        }
    }
}
