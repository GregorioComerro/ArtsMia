import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.buildGraph()
        nNodes, nEdges = self._model.getGraphdetails()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {nNodes} nodi e {nEdges} archi"))
        self._view.update_page()



    def handleCompConnessa(self,e):
        nodo = self._view._txtIdOggetto.value

        if nodo is None:
            self._view.txt_result.controls.append(ft.Text(f"Indicare un id"))

        componente = self._model.getComponenteConnessa(nodo)

        self._view.txt_result.controls.append(ft.Text(f"La componente connessa contiene {len(componente)} vertici."))
        grado = self._model.getGrado(nodo)

        self._view.txt_result.controls.append(
            ft.Text(f"La componente connessa contiene {len(componente)} vertici. Grado nodo: {grado}")
        )

        idNodo, grado = self._model.getPrimoNodoConnesso()
        self._view.txt_result.controls.append(
            ft.Text(f"Prova con id {idNodo}, grado {grado}")
        )

        self._view.update_page()



