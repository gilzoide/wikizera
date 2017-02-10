/// Auxiliar que dá bind em métodos pelo seu nome, pra ficar um poquinho menos
// feio as classes (um tikim menos código também
export default function bindMethod (obj, funcName) {
	obj[funcName] = obj[funcName].bind (obj);
}
