ECHO가 설정되어 있습니다.
package guguadan;

public class gugudan {
	public static void main(String[] args) {
		
		int gu;
		int gugudan;
		
		Scanner s= new Scanner(System.in);
		System.out.printf("출력할 단을 입력하시오 : ");
		gu=s.nextInt();
		
		
		for(int i=0;i<=9,i++) {
			gugudan=i*gu;
			System.out.println(gu+"x"+i+"="+gugudan);
		}
		
		
	}
}