package gugudan;

import java.util.Scanner;
public class gugudan {

public static void main(String[] args) {
		
		int gu;
		int gugudan;
		
		Scanner s= new Scanner(System.in);
		System.out.printf("출력할 단을 입력하시오 : ");
		gu=s.nextInt();
		
		for(int i=2;i<=9;i++) {
			gugudan=i*gu;
			System.out.println(i+"x"+gu+"="+gugudan);
				
					
					
				}
				
			
		
		
		

	}

}
