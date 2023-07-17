public class Hero 
{
    private int posX;
    private int posY;
    public string name;
    public int height;
    public int weight;
    public string color;
    public int speed;
    public int jumpPower;

    public Hero(string name ="Janek", int height = 150, int weight = 50, string color = "yellow", int speed = 2, int jumpPower = 2)
    {
        this.name = name;
        this.height = height;
        this.weight = weight;
        this.color = color;
        this.speed = speed;
        this.jumpPower = jumpPower;

        this.posX = rand(1,255);
        this.posY = rand(1,255);
    }

    
    public void MoveRight() {
        this.posX = (this.posX + this.speed)%255;
    }
    
    public void MoveLeft(){
        this.posX = (this.posX - this.speed)%255;
    }

    public void MoveUp(){
        this.posY = (this.posY + this.jumpPower)%255;
    }

    public void MoveDown(){
        this.posY = (this.posY - this.jumpPower)%255;
    }
}


public void main(){

    var hero1 = new Hero("Mario", 110, 80, "red", 3, 1);
    var hero2 = new Hero("Luigi", 170, 55, "green", 1, 3);

    var hero3 = new Hero(name = "Talarek");

    switch (input):
        case RightArrow:
            hero1.MoveRight();
            break;
        case LeftArrow:
            hero1.MoveLeft();
            break;
        case UpArrow:
            hero1.MoveUp();
            break;
        case KeyD:
            hero2.MoveRight();
            break;
        case KeyA:
            hero2.MoveLeft();
            break;
        case KeyW:
            hero2.MoveUp();
            break;
    
}