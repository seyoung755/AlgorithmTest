/*
 * Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
 * Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
 * Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
 * Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
 * Vestibulum commodo. Ut rhoncus gravida arcu.
 */

import java.util.Arrays;

public class QuickSort {
    private static void swap(int[] a, int i, int j) {
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }

    private static int partition(int[] arr, int lo, int hi) {

        int pivot = arr[hi]; // 맨 오른쪽 값을 pivot으로 정함
        int left = lo; // 투 포인터 이용
        int right;
        for (right = lo; right < hi; right++) {
            /*
            오른쪽 포인터를 이동하다가 pivot보다 작은 숫자가 등장하면
            왼쪽 포인터(pivot보다 큰 숫자임이 보장됨)의 값과 교환하고
            왼쪽 포인터를 하나 이동시킨다.
            */

            if (arr[right] < pivot) {
                swap(arr, right, left);
                left += 1;
            }

        }

        // 마지막으로 확인된 left의 위치와 pivot값을 교환한다.
        // left 값은 어쨌든 pivot보다 큰 숫자임을 뜻하므로 pivot의 위치는 정렬이 된 것을 알 수 있다.
        // 즉, 퀵 정렬은 한번에 pivot 값만 정렬된다.
        // 정렬된 pivot을 기준으로 왼쪽, 오른쪽으로 나눠 분할정복 방식으로 정렬시켜 올라온다.
        swap(arr, hi, left);

        return left;
    }

    public static void rightPivotSort(int[] arr, int lo, int hi) {

        // 분할 정복 완료
        if (lo >= hi) {
            return;
        }

        int pivot = partition(arr, 0, hi);

        // pivot을 기준으로 좌우로 분할
        rightPivotSort(arr, lo, pivot - 1);
        rightPivotSort(arr, pivot + 1, hi);
    }

    public static void main(String[] args) {

        /* 퀵 정렬의 특징
        - 시간 복잡도 : 최악의 경우에 O(n^2), pivot이 최솟값이 최댓값을 설정되는 경우
            - 하지만 일반적으로 O(nlogn)의 성능을 가지며, O(nlogn)의 정렬 중 가장 빠르다.
        - 추가 메모리 없이 정렬이 가능하다 -> 제자리 정렬이다.
        - Unstable sort이다 -> stable로 만들기 위해서는 O(n)의 추가 메모리가 필요하다.
        - 이미 정렬된 배열에 대해서는 불균형 분할에 의해 시간이 더 오래 걸린다.
         */

        System.out.println("Quick sort");
        int[] arr = {3, 7, 2, 4, 1, 9, 6};
        rightPivotSort(arr, 0, arr.length - 1);
        System.out.println(Arrays.toString(arr));
    }
}
