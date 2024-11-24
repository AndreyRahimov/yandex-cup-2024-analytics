from new_civilizations import new_civilizations
from persons import persons

# count = 0
# to_delete = set()
# to_add = []
#
# print(len(new_civilizations[0]))
#
# for person in new_civilizations[0]:
#     for i in range(1, len(new_civilizations)):
#         if person in new_civilizations[i]:
#             to_add.extend(new_civilizations[i])
#             to_delete.add(i)
#             count += 1
#             continue
#
# print(len(to_add))
# new_civilizations[0].extend(to_add)
# print(len(to_delete))
# print(count)
# print(len(new_civilizations[0]))
# print(to_delete)
# new_civilizations[0] = list({*new_civilizations[0]})
# print(len(new_civilizations[0]))

# new_civilizations = [{*new_civilization} for new_civilization in new_civilizations]
#
# print(len(new_civilizations))
# print(new_civilizations)
#
# to_delete = set()
#
# for i in range(len(new_civilizations)):
#     for j in range(i + 1, len(new_civilizations)):
#         if new_civilizations[i] < new_civilizations[j]:
#             to_delete.add(i)
#
#         elif new_civilizations[j] <= new_civilizations[i]:
#             to_delete.add(j)
#
# print(to_delete)
# print(len(to_delete))
# #
# new_civilizations = [list(new_civilizations[i]) for i in range(len(new_civilizations)) if i not in to_delete]
# print(new_civilizations)
# print(len(new_civilizations))
#
count = 0
unions = {}

for i in range(len(new_civilizations) - 1):
    for j in range(i + 1, len(new_civilizations)):
        for person in new_civilizations[i]:
            if person in new_civilizations[j]:
                unions.setdefault(i, []).append(j)
                count += 1
                print(count)
#
# for key, value in unions.items():
#     for n in value:
#         new_civilizations[key].extend(new_civilizations[n])
#
# print(len(new_civilizations))
#
# new_civilizations = [{*new_civilization} for new_civilization in new_civilizations]
# new_civilizations = [list(new_civilization) for new_civilization in new_civilizations]
#
# print(new_civilizations)
# print(len(new_civilizations))
