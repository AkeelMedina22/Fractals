String str = "AB";
int N = 300;

void setup()
{
   size(600,600);
   loadPixels();
   
   for (int i = 0; i < width; i++)
   {
     for (int j = 0; j < height; j++)
     {
       float rn = 0;       
       int iter = 0;
       float lambda = 0;
       float xn = 0.5;
       
       int index = i + j * width;
       float pointx = map(i, 0, height, 2, 4);
       float pointy = map(j, 0, width, 2, 4);
   
       for (int z = 0; z < N; z++)
       {
         char r = str.charAt(iter);
         iter += 1;
         iter = iter % str.length();         
         
        if (r == 'A')
         {
           rn = pointx;
         }
         else if (r == 'B')
         {
           rn = pointy;
         }
         
         xn = rn * xn * (1-xn);
         
         lambda += log(abs(rn* (1-2*xn))) / N / log(2);
         
       }
       
       if (lambda < 0)
       {
         float intensity = map(lambda, -1, 0, 0, 255);
         //pixels[index] = color(intensity/10, intensity/10, intensity/10);
         pixels[index] = color(intensity, intensity, 0);
       }
       if (lambda > 0)
       {
         float intensity = map(lambda, 0, 1.5, 0, 255);
         //pixels[index] = color(intensity*2, intensity*2, intensity*2); 
         pixels[index] = color(0, 0, intensity);
       }

     }
   }
   updatePixels();
}
