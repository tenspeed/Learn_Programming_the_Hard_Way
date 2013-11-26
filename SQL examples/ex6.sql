SELECT pet.id, pet.name, pet.age, pet.dead
	FROM pet, person, person_pet
	WHERE
	pet.id = person_pet.pet_id AND
	person_pet.person_id = person.id AND
	person.first_name = "Zed";