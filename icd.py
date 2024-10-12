if __name__ == "__main__":
    import icd10

    # print(icd10.codes)
    # print(len(icd10.codes))

    # disease only
    disease_chapters = {'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII'}

    chapter_counter = {}
    for code in icd10.codes:
        try:
            data = icd10.find(code)
            chapter = data.chapter
            # if chapter is None:
            #     print(data.description)

            if chapter not in disease_chapters:
                continue

            if chapter not in chapter_counter:
                chapter_counter[chapter] = 1
            else:
                chapter_counter[chapter] += 1
            print(code, data.description)
        except Exception as e:
            pass
            # print(e)
            # print(code, data.description)

    print(chapter_counter)


    print(icd10.chapters)
    print(code.description)  # Acute bronchitis due to Mycoplasma pneumoniae
    if code.billable:
        print(code, "is billable")  # J20.0 is billable

    print(code.chapter)  # X
    print(code.block)  # J00-J99
    print(code.block_description)