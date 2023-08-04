import java.util.ArrayList;

public class HashTable {

	private static final String DELETED = "DELETED";
	//private ArrayList<Person> conglomerate;
	private ArrayList<Person>[] table;
	//private Person[] table;
	private int size;

	public HashTable() {
		this.table = new ArrayList[20];
	}

	public int hash(int key) {
		return key % this.table.length;
	}

	public Person get(int key) {
		
		int hash = hash(key);
		ArrayList<Person> people = this.table[hash];

		if (people == null) {
			return null;
		}

		for (Person p : people) {
			if (p.cpf == key) {
				return p;
			}
		}
		
		return null;

		//int hash = hash(key);
		//return this.table[hash];
	}

	public void put(int key, Person person) {
		if (key == null || person == null) throw new NullPointerException();

		int hash = hash(key);
		ArrayList<Person> people = this.table[hash];

		if (people == null) {
			people = new ArrayList<Person>();
			people.add(person);
			this.table[hash] = people;
		} else {
			people
		}

		if (this.get(key) == null) {
			people.add(Person);
		} else {
			people.get(key).value = person.value;
		}


		//int hash = hash(key);
		//this.table[hash] = person;
	}

	public Person remove(int key) {
		int hash = hash(key);
		Person p = this.table[hash];
		this.table[hash] = DELETED;
		return p;
	}

	// delete/remove
	// resize and rehash
	// contains
	//
}

