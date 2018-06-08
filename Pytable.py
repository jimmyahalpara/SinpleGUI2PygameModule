'''This module can be create tables in python to better represent the data. This cant be used as database. You can create organise date in table formed of +, |, and -.
made by jimmy kumar ahalpara'''
class Pytable:
    def __init__(self,table_name='Table'):
        '''initiator method, table name should be a string'''
        if type(table_name)==str:
            self.__max_row=0
            self.table_name=table_name
            self.__main_dict={}
            self.__sequence=[]
        else:
            raise TypeError('table_name must be a string')
    def insert_column(self,heading):
        '''used to insert column, enter column heading'''
        heading=str(heading)
        self.__main_dict[heading]=[len(heading),[]]
        self.__sequence.append(heading)
    def swap_column_position(self,first_col_name,second_col_name):
        '''swap two column using their name'''
        if (first_col_name in self.__sequence) and (second_col_name in self.__sequence):
            first_col_name,second_col_name=str(first_col_name),str(second_col_name)
            i1=self.__sequence.index(first_col_name)
            i2=self.__sequence.index(second_col_name)
        else:
            raise KeyError('column name not found')
            self.__sequence[i1],self.__sequence[i2]=self.__sequence[i2],self.__sequence[i1]
    def swap_cells(self,column_name,cel1,cel2):
        '''swap cells using their value'''
        column_name,cel1,cel2=str(column_name),str(cel1),str(cel2)        
        if (cel1 in self.__main_dict[column_name][1]) and (cel2 in self.__main_dict[column_name][1]):
            i1=self.__main_dict[column_name][1].index(cel1)
            i2=self.__main_dict[column_name][1].index(cel2)
            k=self.__main_dict[column_name][1][i1]
            self.__main_dict[column_name][1][i1]=self.__main_dict[column_name][1][i2]
            self.__main_dict[column_name][1][i2]=k
        else:
            raise KeyError('cell name not found')
    def insert_into_column(self,column_name,value):
        '''insert values into column'''
        column_name=str(column_name)
        value=str(value)
        if column_name in self.__sequence:
            self.__main_dict[column_name][1].append(value)
            if len(value)>self.__main_dict[column_name][0]:
                self.__main_dict[column_name][0]=len(value)
            if len(self.__main_dict[column_name][1])>self.__max_row:
                self.__max_row=len(self.__main_dict[column_name][1])
        else:
            raise KeyError('column name not found')
    def insert_by_index(self,column_name,index,value):
        '''insert into column by their index'''
        value=str(value)
        if column_name in self.__sequence:
            if type(index)==int:
                self.__main_dict[column_name][1].insert(index,value)
                if len(value)>self.__main_dict[column_name][0]:
                    self.__main_dict[column_name][0]=len(value)
                if len(self.__main_dict[column_name][1])>self.__max_row:
                    self.__max_row=len(self.__main_dict[column_name][1])
            else:
                raise TypeError('index must be a number')
        else:
            raise KeyError('column name not found')
    def return_sheet(self):
        '''will return a string, printing that string will result in formation of table using  + and -'''
        st=self.table_name+'\n'
        st+='+'
        for a in self.__sequence:
            st+='-'*self.__main_dict[a][0]+'+'
        st+='\n|'
        for a in self.__sequence:
            st+=a+' '*(self.__return_diff(len(a),self.__main_dict[a][0]))+'|'
        st+='\n+'
        for a in self.__sequence:
            st+='-'*self.__main_dict[a][0]+'+'
        for a in range(self.__max_row):
            st+='\n|'
            for b in self.__sequence:
                st+=self.__return_from_list(b,a)+(' '*(self.__return_diff(len(self.__return_from_list(b,a)),self.__main_dict[b][0])))+'|'
            st+='\n+'
            for b in self.__sequence:
                st+=('-'*self.__main_dict[b][0])+'+'
        return st
    def __return_diff(self,a,b):
        if a>=b:
            return a-b
        elif b>a:
            return b-a
    def __return_max(self,a,b):
        if a>b:
            return a
        else:
            return b
    
    def __return_from_list(self,column,ind):
        try:
            value=self.__main_dict[column][1][ind]
        except IndexError:
            value=' '
        return value
    def delete_column(self,column_name):
        '''delete column using their column name'''
        column_name=str(column_name)
        if column_name in self.__sequence:
            self.__sequence.remove(column_name)
            del self.__main_dict[column_name]
        else:
            raise KeyError('column name not found')
    def delete_cell(self,column_name,value):
        '''delete of a collumn using their cell value of index number'''
        column_name=str(column_name)
        if column_name in self.__sequence:
            if type(value)==str:
                if value in self.__main_dict[column_name][1]:
                    self.__main_dict[column_name][1].remove(value)
            elif type(value)==int:
                if value < len(self.__main_dict[column_name][1]):
                    del self.__main_dict[column_name][1][value]
            else:
                raise TypeError('value must be a string or integer')
        else:
            raise KeyError('column name not found')
        ma=0
        for a in self.__main_dict:
            if len(self.__main_dict[a][1])>ma:
                ma=len(self.__main_dict[a][1])
        self.__max_row=ma
                

