using System;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Threading;

namespace Game_Assignment
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        //This is to check if the player is pressing the keys when moving
        bool goLeft, goRight, goUp, goDown;
        //Initialize player speed
        int speed = 5;
        //Timer that will be used for whenever the player is moving
        DispatcherTimer timer = new DispatcherTimer();

        //Create game object
        Game game;

        //Make our character
        Wizard wizard;
        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            //Initialize game
            game = new Game();

            Map map = new Map();
            //Going to create 5 force fields (Cover) around the environment as cover
            for (int i = 0; i < 5; i++) {
                //Create Image for the force field
                Image forceField = new Image();

                //Set the image for the force field
                BitmapImage logo = new BitmapImage();
                logo.BeginInit();
                logo.UriSource = new Uri("pack://application:,,,/Images/shield.png");
                logo.EndInit();
                forceField.Source = logo;

                forceField.Width = 54;
                forceField.Height = 54;

                //Randomly place within the canvas
                Canvas.SetLeft(forceField, new Random().Next(0,(int)canvasImg.ActualWidth - 40));
                Canvas.SetTop(forceField, new Random().Next(0,(int)canvasImg.ActualHeight - 40));

                //Add the image to the canvas (game environment)
                canvasImg.Children.Add(forceField);
            }

            // === Implement obstacle (for example lava) ===
            for (int i = 0; i < 5; i++)
            {
                //Implement here

            }

            //Set staff min and max damage
            MagicStaff magicStaff = new MagicStaff(10, 20);

            //The Different classes (inherited from player)
            //The wizard carries the magic staff
            wizard = new Wizard(magicStaff, player);

            //List the players in the game environment
            game.players.Add(wizard);

            //Display the character's stats (in this case view our wizard character's stats)
            RenderPlayerStats();

            //Render the position of player
            RenderPos();

            //Control scheme
            string nl = Environment.NewLine;
            controlScheme.Text += $"{nl}F to barehand attack{nl}Z to attack with weapon";
        }
        public MainWindow()
        {
            InitializeComponent();

            //Focus on the canvas image
            canvasImg.Focus();

            //New event handler responsible for the timer that is used for movement in sprites
            timer.Tick += Timer_Tick;
            //This is the period between each interval from ticks
            timer.Interval = TimeSpan.FromMilliseconds(1);
            //Start the timer
            timer.Start();
        }

        private void Window_PreviewKeyDown(object sender, KeyEventArgs e)
        {
            //Close application if the "ESC" button has been pressed
            if (e.Key == Key.Escape)
                this.Close();
        }
        private void Timer_Tick(object sender, EventArgs e)
        {
            //Check if the player is not dead
            if (wizard.health > 0)
            {
                if (goUp && Canvas.GetTop(player) > 0)
                {
                    //If go up is true and player is within the boundary from the top 
                    //then we can use the set top to move the player towards top of the screen
                    Canvas.SetTop(player, Canvas.GetTop(player) - speed);

                    //This is just for getting the position of player
                    RenderPos();
                }
                if (goDown && Canvas.GetTop(player) + (player.Height * 2) < Application.Current.MainWindow.Height)
                {
                    //If go down is true and player is within the boundary from the bottom of the screen
                    //then we can set top of player to move down
                    Canvas.SetTop(player, Canvas.GetTop(player) + speed);

                    RenderPos();
                }
                if (goLeft && Canvas.GetLeft(player) > 0)
                {
                    //If go left is true and player is inside the boundary from the left
                    //then we can set left of the player to move towards left of the screen
                    Canvas.SetLeft(player, Canvas.GetLeft(player) - speed);

                    //Change sprite character to move left
                    BitmapImage logo = new BitmapImage();
                    logo.BeginInit();
                    logo.UriSource = new Uri("pack://application:,,,/Images/wizard.png");
                    logo.EndInit();
                    player.Source = logo;

                    RenderPos();
                }
                if (goRight && Canvas.GetLeft(player) + (player.Width) < Application.Current.MainWindow.Width)
                {
                    //If go right is true and player is inside the boundary from the right
                    //then we can set left of the player to move towards right of the screen
                    Canvas.SetLeft(player, Canvas.GetLeft(player) + speed);

                    //Change sprite character to move right
                    BitmapImage logo = new BitmapImage();
                    logo.BeginInit();
                    logo.UriSource = new Uri("pack://application:,,,/Images/wizard1.png");
                    logo.EndInit();
                    player.Source = logo;

                    RenderPos();
                }
            }
        }

        private void canvasImg_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.S)
                goDown = true;
            if (e.Key == Key.W)
                goUp = true;
            if (e.Key == Key.A)
                goLeft = true;
            if (e.Key == Key.D)
                goRight = true;

            //Attack actions
            if (wizard.health > 0)
            {
                if (e.Key == Key.F)
                {
                    //Attack barehand (this will attack yourself!)
                    Player attackedPlayer = wizard;
                    wizard.attack(attackedPlayer);
                    //Log the actions
                    Log($"{wizard.ClassType} attacked {attackedPlayer.GetType().Name} with fists!{Environment.NewLine}");
                    if (attackedPlayer.health <= 0)
                        Log($"{attackedPlayer.GetType().Name} was killed!");
                    //Re-render the stats after action
                    RenderPlayerStats();
                }
                if (e.Key == Key.Z)
                {
                    //Attack with weapon (this will attack yourself! Just change the 'attackedPlayer' to change target)
                    Player attackedPlayer = wizard;
                    //Attack using the player's weapon
                    wizard.weapon.attack(wizard);
                    //Log the actions
                    Log($"{wizard.ClassType} attacked {attackedPlayer.GetType().Name} with {wizard.weapon.GetType().Name}!{Environment.NewLine}");
                    if (attackedPlayer.health <= 0)
                        Log($"{attackedPlayer.GetType().Name} was killed!");
                    //Re-render the stats after action
                    RenderPlayerStats();
                }
            }

            //Reset game
        }
        private void canvasImg_KeyUp(object sender, KeyEventArgs e)
        {
            //This is resposible for when the key is up then player is not moving
            if (e.Key == Key.S)
                goDown = false;
            if (e.Key == Key.W)
                goUp = false;
            if (e.Key == Key.A)
                goLeft = false;
            if (e.Key == Key.D)
                goRight = false;
        }
        public void RenderPlayerStats()
        {
            //Display all the character text stats info
            string nl = Environment.NewLine;
            CharacterDescription.Text = $"Health: {wizard.health.ToString()}";
            CharacterDescription.Text += $"{nl}Class: {wizard.ClassType}";
            CharacterDescription.Text += $"{nl}Min barehand damage: {wizard.barehandDamageMin.ToString()}";
            CharacterDescription.Text += $"{nl}Max barehand damage: {wizard.barehandDamageMax.ToString()}";
            CharacterDescription.Text +=
                $"{nl}Weapon equipped: {wizard.weapon.GetType().Name} (Min: {wizard.weapon.minDamage}, Max: {wizard.weapon.maxDamage})";

            //Check if the player's health is 0 or below (Game over)
            if (wizard.health <= 0) {
                gameOver.Visibility = Visibility.Visible;
            }
        }
        //Render the position of character
        public void RenderPos() {
            wizard.GetPos(player);
            playerPos.Text = $"X: {wizard.posX} Y: {wizard.posY}";
        }
        //Log the actions in the mini-console
        void Log(string msg)
        {
            logConsole.AppendText(msg);
            logConsole.ScrollToEnd();
        }
    }
}
