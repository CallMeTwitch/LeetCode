class Solution:
    def strongPasswordChecker(self, password):
        l = sum([1 for q in password if q.islower()])
        u = sum([1 for q in password if q.isupper()])
        d = sum([1 for q in password if q.isdigit()])

        n = 0

        for _ in range(6 - len(password)):
            n += 1
            if not l:
                password = self.insert(password, self.triple(password), 'a')
                l = True
            elif not u:
                password = self.insert(password, self.triple(password), 'A')
                u = True
            elif not d:
                password = self.insert(password, self.triple(password), '0')
                d = True
            else:
                i = self.triple(password)
                if password[i] == 'a':
                    password = self.insert(password, i, 'z')
                else:
                    password = self.insert(password, i, 'a')

        for _ in range(len(password) - 20):
            n += 1
            i = self.triple(password)
            if i:
                password = self.delete(password, i)
            else:
                for q in range(len(password)):
                    if password[q].islower():
                        if l - 1:
                            if not self.triple(self.delete(password, q)):
                                password = self.delete(password, q)
                                break
                    
                    elif password[q].isupper():
                        if u - 1:
                            if not self.triple(self.delete(password, q)):
                                password = self.delete(password, q)
                                break
                    
                    else:
                        if d - 1:
                            if not self.triple(self.delete(password, q)):
                                password = self.delete(password, q)
                                break

        password = list(password)

        while (i := self.triple(password)):
            n += 1
            if not l:
                password[i] = 'a'
                l = True
            elif not u:
                password[i] = 'A'
                u = True
            elif not d:
                password[i] = '0'
                d = True
            else:
                if i != len(password) - 1:
                    if password[i - 1] != 'a' and password[i + 1] != 'a':
                        password[i] = 'a'
                    elif password[i - 1] != 'A' and password[i + 1] != 'A':
                        password[i] = 'A'
                    else:
                        password[i] = '0'
                else:
                    if password[i - 1] != 'a':
                        password[i] = 'a'
                    elif password[i - 1] != 'A':
                        password[i] = 'A'
                    else:
                        password[i] = '0'

        for q in range(len(password)):
            if not l:
                if password[q].isupper():
                    if u - 1:
                        password[q] = 'a'
                        n += 1
                        l = True
                elif password[q].isdigit():
                    if d - 1:
                        password[q] = 'a'
                        n += 1
                        l = True
            elif not u:
                if password[q].islower():
                    if l - 1:
                        password[q] = 'A'
                        n += 1
                        u = True
                elif password[q].isdigit():
                    if d - 1:
                        password[q] = '0'
                        n += 1
                        u = True
            elif not d:
                if password[q].islower():
                    if l - 1:
                        password[q] = '0'
                        n += 1
                        d = True
                elif password[q].isupper():
                    if u - 1:
                        password[q] = '0'
                        n += 1
                        d = True
            else:
                break

        return n

    def insert(self, x, y, z):
        return x[:y] + z + x[y:]
    
    def delete(self, x, y):
        return x[:y] + x[(y + 1):]

    def triple(self, password):
        output = []
        n = 0
        temp = []
        while n < len(password) - 2:
            if password[n] == password[n + 1] == password[n + 2]:
                if temp:
                    temp[0] += 1
                else:
                    temp = [3, n]
            else:
                if temp:
                    output += [temp]
                    temp = []
            
            n += 1

        if temp:
            output += [temp]

        if output:
            return min(output, key = lambda x:x[0] % 3)[1] + 2
        else:
            return 0