	private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
		in.registerValidation(new ObjectInputValidation() {
			
			@Override
			public void validateObject() throws InvalidObjectException {
				try {
					Signable.this.verifySignature();
				} catch (Exception e) {
					throw new InvalidObjectException(e.getMessage());
				}
			}
		}, 0);
		
		in.defaultReadObject();
	}
