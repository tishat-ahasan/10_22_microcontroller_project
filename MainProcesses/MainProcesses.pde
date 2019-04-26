import processing.serial.*;
Serial mySerial;
int i=1;
PrintWriter output;
BufferedReader input;

void setup() {
mySerial = new Serial( this, Serial.list()[0], 9600 );


}

//void draw()
//{
//  if (i==1){
//      i++;
//     output = createWriter( "data.txt" );
//    output.print("1");
//    output.close(); 
//    print("yess!");
//  }
//}


void draw() {
  
  if (mySerial.available() > 0 ) {
  i++;
  String value = mySerial.readString();
  println("here 1  "+value);
  
  if (value.equals("a"))
  {
    
    delay(1000);
    output = createWriter( "data.txt" );
    output.print("1");
    output.close();
    
    delay(5000);
    
    input = createReader("result.txt");
    String ans="";
    try{
    ans = input.readLine();
    println(ans);
    input.close();
    }
    catch(Exception e){
      println(e);
    }
    
    
    

    
    println("pathassi ---> ");
    if (ans.equals("2"))
      mySerial.write(2);
    else if (ans.equals("1"))
      mySerial.write(1);
    else
      mySerial.write(0);
  }
  //mySerial.write(1);
  }
  
  
  
  //println("abcd");
  //delay(2000);
  //mySerial.write(i);
  
  //delay(10000);
  //i++;
}
