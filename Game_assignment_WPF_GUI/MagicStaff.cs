using System;
using System.Collections.Generic;
using System.Text;

namespace Game_Assignment
{
    public class MagicStaff : Weapon
    {
        int staffMin, staffMax;
        public MagicStaff(int min, int max) : base(min,max) {
            staffMin = min;
            staffMax = max;
        }
    }
}
