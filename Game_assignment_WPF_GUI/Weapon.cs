using System;
using System.Collections.Generic;
using System.Text;

namespace Game_Assignment
{
    abstract public class Weapon
    {
        //The min and max damage variables
        public int minDamage;
        public int maxDamage;
        //Specify the weapon's minimum and maximum damage
        public Weapon(int min, int max) {
            minDamage = min;
            maxDamage = max;
        }

        //Attack the player and deal damage from weapon
        public void attack(Player player) {
            //Deal damage to player from getting min to max damage
            //Damage will be randomized from range
            player.health -= new Random().Next(minDamage, maxDamage);
        }
    }
}
