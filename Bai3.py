class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    def button_sort_click(self, **event_args):
        numbers = [int(x.strip()) for x in self.text_box_numbers.text.split()]
        sorted_numbers = self.merge_sort(numbers)
        self.label_sorted_numbers.text = " " + ", ".join(map(str, sorted_numbers))

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr

    def text_box_numbers_change(self, **event_args):
        self.label_sorted_numbers.text = ""

    def text_box_numbers_pressed_enter(self, **event_args):
        self.button_sort_click()

    def text_box_numbers_key_press(self, **event_args):
        if event_args['key'] == 'Enter':
            self.button_sort_click()

Form1_1 = Form1