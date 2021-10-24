
public class SelectionSort {

    public static int[] selectionSort(int[] arr) {
        for (int i=0 ; i < arr.length-1 ; i++)
        {
            int indexMin = i;
            for (int j=i+1 ; j < arr.length-1 ; j++)
            {
                if (arr[indexMin] > arr[j]) indexMin = j;
            }
            int temp = arr[indexMin];
            arr[indexMin] = arr[i];
            arr[i] = temp;
        }
        return arr;
    }

    public static void main(String[] args) {
        /* 선택 정렬의 특징
        - 모든 경우에 O(n^2)의 성능을 보여준다.
        - 제자리 정렬이다.
        - 교환 횟수가 적어 이미 역순으로 정렬되어 있는 자료를 그 역순으로 정렬할 때 유용하다.
        - Unstable sort이다. (최솟값을 맨 앞 요소와 무조건 교환하는 구조이므로)
         */
        int[] arr = {6,3,10,-3,-10,0,17};
        int[] result = selectionSort(arr);
        for (int i = 0; i < result.length ; i ++) System.out.println(result[i]);
    }
}
