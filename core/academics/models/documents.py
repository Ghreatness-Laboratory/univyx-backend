categoriesChoices = [

	('notes','Notes'),
	('past_questions','Past Questions'),
	('tutorials','Tutorials')
]

class Document(models.Model):
	title = models.CharField(max_length=30)
	description = models.TextField()
	category = models.CharField(max_length=50, choices=categoriesChoices)
	google_docs_url = models.URLField()
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.title} - {self.category}'