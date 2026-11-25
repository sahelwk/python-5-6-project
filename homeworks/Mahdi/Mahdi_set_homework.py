ahmad = {"Python", "HTML", "CSS", "JavaScript"}

ali = {"Python", "JavaScript", "MySQL", "PHP"}

print("Common Subjects:", ahmad.intersection(ali))

print("Only Ahmad:", ahmad.difference(ali))

print("Only Ali:", ali.difference(ahmad))

print("All Unique Subjects:", ahmad.union(ali))

ahmad.add("React")

print("Ahmad's Updated Subjects:", ahmad)
