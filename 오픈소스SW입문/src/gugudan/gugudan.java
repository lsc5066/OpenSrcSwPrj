package gugudan;

import java.util.Scanner;
public class gugudan {

public static void main(String[] args) {
		
		int gu;
		int gugudan;
		
		Scanner s= new Scanner(System.in);
		System.out.printf("출력할 단을 입력하시오 : ");
		gu=s.nextInt();
		
		if (gu==0) {
			for(int i=2;i<=9;i++) {
				for(int j=1;j<=9;j++) {
					gugudan=i*j;
					System.out.println(i+"x"+j+"="+gugudan);
					
				}
				
			
		}
		
		}
		else if(gu>0) {
			for(int i=1;i<=9;i++) {
				gugudan=gu*i;
				System.out.println(gu+"x"+i+"="+gugudan);
			}
		}else if(gu<0) {
			System.out.println("구구단 출력이 불가능합니다. 음수입니다.");
		}
		
		

	}

}
