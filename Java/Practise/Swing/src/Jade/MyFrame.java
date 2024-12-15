package Jade;

import java.awt.Color;

import javax.swing.ImageIcon;
import javax.swing.JFrame;

public class MyFrame extends JFrame {
    MyFrame() {
        
        this.setTitle("Window");
        this.setSize(420, 420);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setResizable(true);
        this.setVisible(true);

        ImageIcon imageIcon = new ImageIcon("linux.svg");
        this.setIconImage(imageIcon.getImage());
        this.getContentPane().setBackground(new Color(0, 0, 255));
    
    }

}
