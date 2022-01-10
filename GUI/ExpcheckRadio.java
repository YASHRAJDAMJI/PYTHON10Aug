/* <Applet code="ExpcheckRadio" width=300 height=300>
</Applet>*/

public class ExpcheckRadio extends Applet
{
    label hobby,gender;
    checkbox singing,dansing;

    public void inti()
    {
      label1=new label ("singing");
      checkbox1=new checkbox("singing");
      add(label1);
      add(checkbox1);
    }
}