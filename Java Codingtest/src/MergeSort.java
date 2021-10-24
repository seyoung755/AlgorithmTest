/*
 * Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
 * Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
 * Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
 * Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
 * Vestibulum commodo. Ut rhoncus gravida arcu.
 */

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class MergeSort {

    public static ArrayList<Integer> divide(ArrayList<Integer> arr) {

        // 분할 완료
        if (arr.size() <= 1) return arr;

        // 분할할 두개의 리스트 생성
        ArrayList<Integer> left = new ArrayList<>();
        ArrayList<Integer> right = new ArrayList<>();
        int mid = arr.size() / 2;

        for (int i=0 ; i<mid ; i++)
        {
            left.add(arr.get(i));
        }

        for (int j=mid; j<arr.size() ; j++) {
            right.add(arr.get(j));
        }

        left = divide(left);
        right = divide(right);
        return merge(left, right);
    }

    public static ArrayList<Integer> merge(ArrayList<Integer> left, ArrayList<Integer> right) {

        // 병합
        ArrayList<Integer> mArr = new ArrayList<>();
        int l=0, r=0;

        while (l < left.size() && r < right.size()) {

            if (left.get(l) < right.get(r)) {
                mArr.add(left.get(l));
                l++;
            } else {
                mArr.add(right.get(r));
                r++;
            }
        }

        while (l < left.size()) {
            mArr.add(left.get(l));
            l++;
        }

        while (r < right.size()) {
            mArr.add(right.get(r));
            r++;
        }

        return mArr;

    }


    public static void main(String[] args) {

        /* 병합정렬은 주어진 배열을 절반씩 쪼갠다음 더 이상 쪼개지지 않을 때 정렬하면서 올라오는 방식이다
        병합정렬의 특징
        - 시간 복잡도 : 어느 경우에도 O(nlogn)
        - 데이터 크기만큼의 추가 메모리가 필요하다 -> 제자리 정렬이 아니다
            - 제자리 정렬로 구현하는 방법에는 연결리스트로 데이터를 구성하여 인덱스만 변경하는 식으로 정렬하는 방법이 있다.
        - Stable sort이다. (같은 값끼리는 순서가 바뀌지 않는다.)

        */
        Integer[] arr = {6,3,10,-3,-10,0,17};
        ArrayList ll = new ArrayList(Arrays.asList(arr));

        ArrayList<Integer> mergeArr = divide(ll);
        System.out.println(mergeArr);
    }

}
