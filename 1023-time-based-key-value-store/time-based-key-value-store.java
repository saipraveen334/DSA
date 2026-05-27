class TimeMap {

    HashMap<String, List<Pair>> store;

    public TimeMap() {
        store = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {

        store.putIfAbsent(key, new ArrayList<>());

        store.get(key).add(new Pair(value, timestamp));
    }

    public String get(String key, int timestamp) {

        String res = "";

        List<Pair> values = store.getOrDefault(key, new ArrayList<>());

        int l = 0;
        int r = values.size() - 1;

        while (l <= r) {

            int m = l + (r - l) / 2;

            if (values.get(m).timestamp <= timestamp) {

                res = values.get(m).value;

                l = m + 1;

            } else {

                r = m - 1;
            }
        }

        return res;
    }

    class Pair {

        String value;
        int timestamp;

        Pair(String value, int timestamp) {
            this.value = value;
            this.timestamp = timestamp;
        }
    }
}