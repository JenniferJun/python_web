class Puppy:
 def __init__(self):
  print(self)
  print("Puppy is born!!")

  self.name = "";
  self.age =0.1;
  self.breed="Beagle"
  pass

ruffus = Puppy()
print(ruffus.name, ruffus.age, ruffus.breed)