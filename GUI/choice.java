/* <Applet code="choice" width=300 height=300>
</Applet>*/

import java.applet.*;
import java.awt.*;
import java.awt.Event.*;

public class choice extends Applet
{
    choice subject;
     
   public void init()
   {
       subject=new choice();
       subject.add("AJP");
       subject.add("os");
       subject.add("st");
       

    add(subject);
   } 
   
}