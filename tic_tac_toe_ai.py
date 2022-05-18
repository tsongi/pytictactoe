from random import choice, randint

class TicTacToeAI:

    def next_move(self, fields, sign, opponent_sign):
        opponents_field = f" {opponent_sign} "
        empty_field = "   "
        own_field = f" {sign} "
        start = True
        for key in fields:
            if fields[key] != empty_field:
                start = False
        if start:
            moves = ["a1", "c1", "a3", "c3"]
            move = choice(moves)
            fields[move] = own_field
            return fields
        else:
            if fields["b2"] == empty_field and randint(0, 1) == 1:
                fields["b2"] = own_field
                return fields
            else:
                if fields["c3"] == empty_field:
                    if fields["a1"] == own_field and fields["b2"] == own_field:
                        fields["c3"] = own_field
                        return fields
                if fields["a3"] == empty_field:
                    if fields["c1"] == own_field and fields["b2"] == own_field:
                        fields["a3"] = own_field
                        return fields
                if fields["b3"] == empty_field:
                    if fields["b1"] == own_field and fields["b2"] == own_field:
                        fields["b3"] = own_field
                        return fields
                if fields["c3"] == empty_field:
                    if fields["c1"] == own_field and fields["c2"] == own_field:
                        fields["c3"] = own_field
                        return fields
                if fields["a3"] == empty_field:
                    if fields["a1"] == own_field and fields["a2"] == own_field:
                        fields["a3"] = own_field
                        return fields
                if fields["b1"] == empty_field:
                    if fields["a1"] == own_field and fields["c1"] == own_field:
                        fields["b1"] = own_field
                        return fields
                if fields["c1"] == empty_field:
                    if fields["a1"] == own_field and fields["b1"] == own_field:
                        fields["c1"] = own_field
                        return fields
                if fields["a1"] == empty_field:
                    if fields["b1"] == own_field and fields["c1"] == own_field:
                        fields["a1"] = own_field
                        return fields
                if fields["c3"] == empty_field:
                    if fields["a3"] == own_field and fields["b3"] == own_field:
                        fields["c3"] = own_field
                        return fields
                if fields["c1"] == empty_field:
                    if fields["c3"] == own_field and fields["c2"] == own_field:
                        fields["c1"] = own_field
                        return fields
                if fields["c2"] == empty_field:
                    if fields["a3"] == own_field and fields["c3"] == own_field:
                        fields["c2"] = own_field
                        return fields
                if fields["a1"] == empty_field:
                    if fields["a3"] == own_field and fields["a2"] == own_field:
                        fields["a1"] = own_field
                        return fields
                if fields["a2"] == empty_field:
                    if fields["a1"] == own_field and fields["a3"] == own_field:
                        fields["a2"] = own_field
                        return fields
                if fields["c2"] == empty_field:
                    if fields["c1"] == own_field and fields["c3"] == own_field:
                        fields["c2"] = own_field
                        return fields
                if fields["c1"] == empty_field:
                    if fields["c2"] == own_field and fields["c3"] == own_field:
                        fields["c1"] = own_field
                        return fields
                if fields["a1"] == empty_field:
                    if fields["c3"] == own_field and fields["b1"] == own_field:
                        fields["a1"] = own_field
                        return fields
                if fields["c1"] == empty_field:
                    if fields["a3"] == own_field and fields["b2"] == own_field:
                        fields["c1"] = own_field
                        return fields
                if fields["b1"] == empty_field:
                    if fields["b3"] == own_field and fields["b2"] == own_field:
                        fields["b1"] = own_field
                        return fields
                if fields["a1"] == empty_field:
                    if fields["c2"] == own_field and fields["b2"] == own_field:
                        fields["a1"] = own_field
                        return fields
                if fields["c2"] == empty_field:
                    if fields["a2"] == opponents_field and fields["b2"] == opponents_field:
                        fields["c2"] = own_field
                        return fields
                if fields["c3"] != own_field:
                    if fields["a1"] == opponents_field and fields["b2"] == opponents_field:
                        fields["c3"] = own_field
                        return fields
                if fields["a3"] != own_field:
                    if fields["c1"] == opponents_field and fields["b2"] == opponents_field:
                        fields["a3"] = own_field
                        return fields
                if fields["b3"] != own_field:
                    if fields["b1"] == opponents_field and fields["b2"] == opponents_field:
                        fields["b3"] = own_field
                        return fields
                if fields["c3"] != own_field:
                    if fields["c1"] == opponents_field and fields["c2"] == opponents_field:
                        fields["c3"] = own_field
                        return fields
                if fields["a3"] != own_field:
                    if fields["a1"] == opponents_field and fields["a2"] == opponents_field:
                        fields["a3"] = own_field
                        return fields
                if fields["b1"] != own_field:
                    if fields["a1"] == opponents_field and fields["c1"] == opponents_field:
                        fields["b1"] = own_field
                        return fields
                if fields["c1"] != own_field:
                    if fields["a1"] == opponents_field and fields["b1"] == opponents_field:
                        fields["c1"] = own_field
                        return fields
                if fields["a1"] != own_field:
                    if fields["b1"] == opponents_field and fields["c1"] == opponents_field:
                        fields["a1"] = own_field
                        return fields
                if fields["c3"] != own_field:
                    if fields["a3"] == opponents_field and fields["b3"] == opponents_field:
                        fields["c3"] = own_field
                        return fields
                if fields["c1"] != own_field:
                    if fields["c3"] == opponents_field and fields["c2"] == opponents_field:
                        fields["c1"] = own_field
                        return fields
                if fields["c2"] != own_field:
                    if fields["a3"] == opponents_field and fields["c3"] == opponents_field:
                        fields["c2"] = own_field
                        return fields
                if fields["a1"] != own_field:
                    if fields["a3"] == opponents_field and fields["a2"] == opponents_field:
                        fields["a1"] = own_field
                        return fields
                if fields["a2"] != own_field:
                    if fields["a1"] == opponents_field and fields["a3"] == opponents_field:
                        fields["a2"] = own_field
                        return fields
                if fields["c2"] != own_field:
                    if fields["c1"] == opponents_field and fields["c3"] == opponents_field:
                        fields["c2"] = own_field
                        return fields
                if fields["c1"] != own_field:
                    if fields["c2"] == opponents_field and fields["c3"] == opponents_field:
                        fields["c1"] = own_field
                        return fields
                if fields["a1"] != own_field:
                    if fields["c3"] == opponents_field and fields["b1"] == opponents_field:
                        fields["a1"] = own_field
                        return fields
                if fields["c1"] != own_field:
                    if fields["a3"] == opponents_field and fields["b2"] == opponents_field:
                        fields["c1"] = own_field
                        return fields
                if fields["b1"] != own_field:
                    if fields["b3"] == opponents_field and fields["b2"] == opponents_field:
                        fields["b1"] = own_field
                        return fields
                if fields["a1"] != own_field:
                    if fields["c2"] == opponents_field and fields["b2"] == opponents_field:
                        fields["a1"] = own_field
                        return fields
                if fields["c2"] != own_field:
                    if fields["a2"] == opponents_field and fields["b2"] == opponents_field:
                        fields["c2"] = own_field
                        return fields
                empty_fields_list = []
                for key in fields:
                    if fields[key] == empty_field:
                        empty_fields_list.append(key)
                fields[choice(empty_fields_list)] = own_field
                return fields
