import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.IOException;
import java.net.URL;
 
public class ImgDiffPercent
{
  public static void main(String args[])
  {
    BufferedImage img1 = null;
    BufferedImage img2 = null;
    try {
      URL url1 = new URL("http://www.refluxcookbookblog.com/wp-content/uploads/2011/05/Jumbo-and-large-eggs-have-same-size-2-yolks-photo-by-Jamie-Koufman.jpg");
      URL url2 = new URL("http://derek.broox.com/photo/1999-f150-xlt/full/11429/same-size-tires-4-differe.jpg");
      img1 = ImageIO.read(url1);
      img2 = ImageIO.read(url2);
    } catch (IOException e) {
      e.printStackTrace();
    }
    int width1 = img1.getWidth(null);
    int width2 = img2.getWidth(null);
    int height1 = img1.getHeight(null);
    int height2 = img2.getHeight(null);
    if ((width1 != width2) || (height1 != height2)) {
      System.err.println("Error: Images dimensions mismatch. Difference percentage 100");
      System.exit(1);
    }
    long diff = 0;
    for (int y = 0; y < height1; y++) {
      for (int x = 0; x < width1; x++) {
        int rgb1 = img1.getRGB(x, y);
        int rgb2 = img2.getRGB(x, y);
        int r1 = (rgb1 >> 16) & 0xff;
        int g1 = (rgb1 >>  8) & 0xff;
        int b1 = (rgb1      ) & 0xff;
        int r2 = (rgb2 >> 16) & 0xff;
        int g2 = (rgb2 >>  8) & 0xff;
        int b2 = (rgb2      ) & 0xff;
        diff += Math.abs(r1 - r2);
        diff += Math.abs(g1 - g2);
        diff += Math.abs(b1 - b2);
      }
    }
    double n = width1 * height1 * 3;
    double p = diff / n / 255.0;
    System.out.println("diff percent: " + (p * 100.0));
    int p1=(int)p;
    System.out.println("Similarity Rank " + p1);
    
  }
}
