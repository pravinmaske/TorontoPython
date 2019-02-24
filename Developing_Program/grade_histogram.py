import tkinter.filedialog
import grade
a1_filename=tkinter.filedialog.askopenfilename()
a1_file =open(a1_filename,'r')


a1_hist_filename=tkinter.filedialog.asksaveasfilename()
a1_hist_file =open(a1_hist_filename,'w')




# Read the grades into a list
grades= grade.read_grades(a1_file)

# count a grades as per range
range_counts=grade.count_grades_range(grades)

#print(range_counts)
# Write the histogram to the file

grade.write_histogram(range_counts,a1_hist_file)

a1_file.close()
a1_hist_file.close()
