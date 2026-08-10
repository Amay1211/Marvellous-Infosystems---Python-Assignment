import math

def MarvellousEucDistance(p1,p2):
  ans = math.sqrt((p1["x"] - p2["x"])**2 + (p1["x"] - p2["x"])**2)
  return ans

def marvellousClassifire(xCoordinate, yCoordinate, k = 3):
  BORDER = "-" * 50


  data = [
    {"point" : "A", "x" : 1, "y" : 2, "label": "Red"},
    {"point" : "B", "x" : 2, "y" : 3, "label": "Red"},
    {"point" : "C", "x" : 3, "y" : 1, "label": "Blue"},
    {"point" : "D", "x" : 6, "y" : 5, "label": "Blue"},
  ]

  print(BORDER)
  print("Marvellous KNN Classifire")
  print(BORDER)

  print("Distance of all points")

  newPoints = {
    "x": xCoordinate,
    "y": yCoordinate
  }

  for d in data:
    d["distance"] = MarvellousEucDistance(d,newPoints)

  sortedData = sorted(data, key = lambda item: item["distance"])

  nearestDatapoints = sortedData[:k]

  votes = {}

  for neibors in nearestDatapoints:
    label = neibors["label"]
    votes[label] = votes.get(label, 0) + 1

  iMax = 0
  name = ""

  for d in votes:
    if votes[d] > iMax:
      iMax = votes[d]
      name = d

  print("Final Prediction", name)


def main():
  x = int(input("Enter x Coordinate "))
  y = int(input("Enter y Coordinate "))
  k = int(input("Enter K Naibores "))

  marvellousClassifire(x,y, k)

if __name__ == "__main__":
  main()
