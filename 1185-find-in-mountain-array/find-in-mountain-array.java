class Solution {

    public int findInMountainArray(int target, MountainArray mountainArr) {

        int l = 1;
        int r = mountainArr.length() - 2;

        int peak = -1;

        while (l <= r) {

            int m = l + (r - l) / 2;

            int left = mountainArr.get(m - 1);
            int mid = mountainArr.get(m);
            int right = mountainArr.get(m + 1);

            if (left < mid && mid < right) {

                l = m + 1;

            } else if (left > mid && mid > right) {

                r = m - 1;

            } else {

                peak = m;
                break;
            }
        }

        l = 0;
        r = peak;

        while (l <= r) {

            int m = l + (r - l) / 2;

            int val = mountainArr.get(m);

            if (val > target) {

                r = m - 1;

            } else if (val < target) {

                l = m + 1;

            } else {

                return m;
            }
        }

        l = peak + 1;
        r = mountainArr.length() - 1;

        while (l <= r) {

            int m = l + (r - l) / 2;

            int val = mountainArr.get(m);

            if (val > target) {

                l = m + 1;

            } else if (val < target) {

                r = m - 1;

            } else {

                return m;
            }
        }

        return -1;
    }
}