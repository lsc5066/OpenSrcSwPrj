ECHO�� �����Ǿ� �ֽ��ϴ�.
package guguadan;

public class gugudan {
	public static void main(String[] args) {
		
		int gu;
		int gugudan;
		
		Scanner s= new Scanner(System.in);
		System.out.printf("����� ���� �Է��Ͻÿ� : ");
		gu=s.nextInt();
		
		
		for(int i=0;i<=9,i++) {
			gugudan=i*gu;
			System.out.println(gu+"x"+i+"="+gugudan);
		}
		
		
	}
}