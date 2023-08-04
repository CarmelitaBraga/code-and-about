public void put(key, value) {
	if (this.isFull()) this.resize();
	int hash = hash(key);
	while (this.table[hash] != null && this.table[hash] != DELETED && this.table[hash].key != key) {
		hash = (hash + 1) % this.table.length;
	}
	this.table[hash] = value;
}
