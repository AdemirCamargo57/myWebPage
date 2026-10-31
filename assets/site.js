document.querySelectorAll('[data-print]').forEach(button => button.addEventListener('click', () => window.print()));
const article = document.querySelector('[data-lesson]');
const toc = document.querySelector('[data-toc]');
if (article && toc) {
  article.querySelectorAll('h2,h3').forEach((heading, i) => {
    if (!heading.id) heading.id = `section-${i + 1}`;
    const item = document.createElement('li');
    const link = document.createElement('a');
    link.href = `#${heading.id}`;
    link.textContent = heading.textContent;
    item.append(link); toc.append(item);
  });
  if (!toc.children.length) document.querySelector('.lesson-toc').hidden = true;
}
const search = document.querySelector('#publication-search');
if (search) {
  const year = document.querySelector('#publication-year');
  const type = document.querySelector('#publication-type');
  const records = [...document.querySelectorAll('[data-publication]')];
  const normalize = text => text.normalize('NFD').replace(/\p{Diacritic}/gu, '').toLocaleLowerCase('en-US');
  const filter = () => {
    const terms = normalize(search.value).trim().split(/\s+/).filter(Boolean);
    let visible = 0;
    records.forEach(record => {
      const match = (!year.value || record.dataset.year === year.value) && (!type.value || record.dataset.type === type.value) && terms.every(term => normalize(record.textContent).includes(term));
      record.hidden = !match; if (match) visible++;
    });
    document.querySelectorAll('[data-publication-year]').forEach(section => { section.hidden = !section.querySelector('[data-publication]:not([hidden])'); });
    document.querySelector('[data-publication-count]').textContent = `${visible} of ${records.length} records`;
    document.querySelector('[data-no-results]').hidden = visible !== 0;
  };
  search.addEventListener('input', filter); year.addEventListener('change', filter); type.addEventListener('change', filter);
}
