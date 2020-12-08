from WhiskeyDAO import WhiskeyDAO


#returnValue = bookDao.create(book)
returnValue = WhiskeyDAO.getAll()
print(returnValue)
returnValue = WhiskeyDAO.findById(10437)
print("find By Id")
print(returnValue)
returnValue = WhiskeyDAO.update(10437)
print(returnValue)
returnValue = WhiskeyDAO.findById(10437)
print(returnValue)
returnValue = WhiskeyDAO.delete(id)
print(returnValue)
returnValue = WhiskeyDAO.getAll()
print(returnValue)