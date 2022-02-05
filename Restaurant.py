from Table import Table


class Restaurant:

    name: str

    def __init__(self, name, table4count, table2count, locality):
        self.table4s = []
        self.table2s = []
        self.name = name
        self.locality = locality

    def add_table(self, table: Table):
        if table.size == 2:
            self.table2s += table
        elif table.size == 4:
            self.table4s += table
        else:
            print("Please enter a valid table i.e. of size 2 or 4")

    def occupy_table(self, table: Table):
        if table.size == 2:
            for table in self.table2s:
                if table.occupied is False:
                    table.occupied = True
                    return

            print("All tables are already occupied")
            return

        elif table.size == 4:
            for table in self.table4s:
                if table.occupied is False:
                    table.occupied = True
                    return
            print("All tables are already occupied")
            return
        else:
            print("Please enter a valid table i.e. of size 2 or 4")

    def vacate_table(self, table: Table):
        if table.size == 2:
            for table in self.table2s:
                if table.occupied is True:
                    table.occupied = False
                    return
            print("No table is occupied")
            return

        elif table.size == 4:
            for table in self.table4s:
                if table.occupied is True:
                    table.occupied = False
                    return
            print("No table is occupied")
            return
        else:
            print("Please enter a valid table i.e. of size 2 or 4")


    def get_vacancy_info(self) -> dict:
        """ Returns the tables and seats available"""
        table4a = 0
        table4o = 0
        table2a = 0
        table2o = 0
        info = {
            "table for 4 available": table4a,
            "table for 4 occupied": table4o,
            "table for 2 available": table2a,
            "table for 2 occupied": table2o,
        }

        for table in self.table4s:
            if table.occupied:
                table4o += 1
            else:
                table4a += 1

        for table in self.table2s:
            if table.occupied:
                table2o += 1
            else:
                table2a += 1
        return info


