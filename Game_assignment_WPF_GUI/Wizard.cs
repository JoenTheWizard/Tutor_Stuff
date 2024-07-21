using System;
using System.Collections.Generic;
using System.Text;
using System.Windows.Controls;

namespace Game_Assignment
{
    public class Wizard : Player
    {
        public string ClassType;
        public Weapon weapon;
        public double posX, posY;
        public Wizard() {
            ClassType = "Wizard";
        }
        public Wizard(Weapon weapon_) {
            ClassType = "Wizard";
            weapon = weapon_;
        }
        public Wizard(Weapon weapon_, Image player)
        {
            ClassType = "Wizard";
            weapon = weapon_;
            posX = Canvas.GetLeft(player);
            posY = Canvas.GetTop(player);
        }
        public void GetPos(Image player)
        {
            posX = Canvas.GetLeft(player);
            posY = Canvas.GetTop(player);
        }
    }
}
