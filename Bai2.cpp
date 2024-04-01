#include <stdio.h>

// Hàm kiểm tra số chính phương
int laSoChinhPhuong(int num)
{
	int i = 1;
	while (i * i <= num)
	{
		if (i * i == num)
		{
			return 1;
		}
		i++;
	}
	return 0;
}

// Hàm đếm số chính phương và in ra các số đó
void demVaInSoChinhPhuong(int n)
{
	printf("Cac ss chinh phuong nho hon %d la:\n", n);
	for (int i = 1; i < n; i++)
	{
		if (laSoChinhPhuong(i))
		{
			printf("%d, ", i);
		}
	}
	printf("\n");
}

int main()
{
	int n;
	do {
		printf("Nhap vao so nguyen duong n: ");
		scanf("%d", &n);
		if (n <= 0)
		{
			printf("Vui long nhap mot so nguyen duong.\n");
		}
	} while (n <= 0);

	demVaInSoChinhPhuong(n);

	return 0;
}
