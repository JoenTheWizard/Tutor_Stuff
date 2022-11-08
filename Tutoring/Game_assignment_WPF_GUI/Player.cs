using System;
using System.Collections.Generic;
using System.Text;

namespace Game_Assignment
{
    //This has to be abstract
    //The player class is going to be used for players and enemies
     abstract public class Player
    {
        public int health;
        //public Weapon weapon;
        public int barehandDamageMin;
        public int barehandDamageMax;

        //Constructor
        public Player() {
            health = 100;
            barehandDamageMin = 10; 
            barehandDamageMax = 15;
        }

        public int Health() {
            return health;
        }

        //Attack player
        public void attack(Player player) {
            player.health -= new Random().Next(barehandDamageMin, barehandDamageMax);
        }
    }
}
