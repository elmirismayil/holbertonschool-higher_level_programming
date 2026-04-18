#!/usr/bin/env python3

class VerboseList(list):
    """A class that extends list and notifies when items are added or removed."""

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        """Extends the list and prints how many items were added."""
        items_count = len(x)
        super().extend(x)
        print(f"Extended the list with [{items_count}] items.")

    def remove(self, item):
        """Prints notification before removing an item."""
        # Qeyd: super().remove(item) xəta verərsə (item yoxdursa), 
        # mesaj çap olunmamalıdır. Ona görə mesajı silinmə uğurlu olduqda çap edirik.
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Prints notification before popping an item."""
        # İndeks üzrə elementi tapırıq ki, mesajda göstərə bilək
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
