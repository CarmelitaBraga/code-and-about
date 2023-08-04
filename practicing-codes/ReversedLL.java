public class ReversedLL {

        private Node head;

        public ReversedLL(Node head) {
                this.head = head;

        }

        public void add(String v) {
                Node aux = head;

                if (aux == null) {
                        head = new Node(v);
                } else {
                        while (aux.next != null) {
                                aux = aux.next;
                        }
                        aux.next = new Node(v);
                }
        }

        public String toString() {
                String s = "";
                Node aux = this.head;
                while (aux != null) {
                        s += aux.value + " ";
                        aux = aux.next;
                }
                return s.trim();
        }


        public void doIt(String v) {
                this.add(v);
                if (this.head.next != null) reverse(this.head, null);
        }

        private void reverse(Node current, Node next) {
                if (current != null) {
                        Node aux = current.next;
                        current.next = next;
                        reverse(next, aux);
                }
                this.head = next;
                //this.head.setNext(null);

        }

        public static void main(String[] args) {

                ReversedLL l = new ReversedLL(new Node("A"));
                System.out.println(l.toString());
                //assert("A", l.toString());

                l.add("B");

                //assert("A B", l.toString());
        }
}










class Node {

        protected Node next;
        protected String value;

        public Node(String value) {
                this.value = value;
        }
}













/*public class ReversedLL {

	private Node head;

	public ReversedLL(Node head) {
		this.head = head;
	
	}

	public static void add(String v) {
		Node aux = this.head;

		if (aux == null) {
			this.head = new Node(v);
		} else {
			while (aux.next != null) {
				aux = aux.next;
			}
			aux.next = new Node(v);
		}
	}

	public static String toString() {
		String s = "";
		Node aux = this.head;
		while (aux != null) {
			s += aux.value + " ";
			aux = aux.next;
		}
		return s.trim();
	}


	public static void doIt(String v) {
		this.add(v);
		if (this.head.next != null) reverse(this.head, null);
	}

	private void reverse(Node current, Node next) {
		if (current != null) {
			Node aux = current.next;
			current.next = next;
			reverse(next, aux);
		}
		this.head = next;
		//this.head.setNext(null);

	}

	public static void main(String[] args) {

		ReversedLL lista = new ReversedLL(new Node("A"));

		assert("A", lista.toString());

		lista.add("B");

		assert("A B", lista.toString());
	}
}










class Node {

	protected Node next;
	protected String value;

	public Node(String value) {
		this.value = value;
	}
}*/
