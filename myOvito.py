from ovito.io import import_file
from ovito.modifiers import *
from ovito.vis import Viewport
from ovito.vis import ParticlesVis
from ovito.qt_compat import QtCore
from ovito.qt_compat import QtGui
from ovito.vis import *
import math


def ovitoMain1():
    pipeline = import_file("wire_melt_500000.dump")
    pipeline.add_to_scene()
    pipeline.modifiers.append(ExpressionSelectionModifier(expression='melted == 0'))
    pipeline.modifiers.append(DeleteSelectedModifier())
    data = pipeline.compute()

    sli1 = []
    sli2 = []
    sli3 = []
    pos_property = data.particles.positions

    for pos in pos_property:
      sli1.append(pos[0])
      sli2.append(pos[1])
      sli3.append(pos[2])

    maX1 = max(sli1)
    miX2 = min(sli1)
    maY1 = max(sli2)
    miY2 = min(sli2)
    maZ1 = max(sli3)
    miZ2 = min(sli3)

    print(f"Длина : {(maX1 - miX2)}, max: {maX1}, min: {miX2}")
    print(f"Высота : {(maY1 - miY2)}, max: {maY1}, min: {miY2}")
    print(f"Ширина : {(maZ1 - miZ2)}, max: {maZ1}, min: {miZ2}")

    pipeline.modifiers.clear()

    vis_element = pipeline.source.data.particles.vis
    vis_element.shape = ParticlesVis.Shape.Square
    vis_element.radius = 0.0001

    # bar_length = 40
    # bar_color = QtGui.QColor(0, 0, 0)
    # label_text = f"{bar_length / 10} nm"
    # label_color = QtGui.QColor(255, 255, 255)

    # def render(args):
    #     if args.is_perspective:
    #         raise Exception("This overlay only works with non-perspective viewports.")
    #
    #     # Compute length of bar in screen space
    #     screen_length = args.project_size((0, 0, 0), bar_length)
    #
    #     # Define geometry of bar in screen space
    #     height = 0.07 * args.painter.window().height()
    #     margin = 0.02 * args.painter.window().height()
    #     rect = QtCore.QRectF(margin, margin, screen_length, height)
    #
    #     # Render bar rectangle
    #     args.painter.fillRect(rect, bar_color)
    #
    #     # Render text label
    #     font = args.painter.font()
    #     font.setPixelSize(height)
    #     args.painter.setFont(font)
    #     args.painter.setPen(QtGui.QPen(label_color))
    #     args.painter.drawText(rect, QtCore.Qt.AlignCenter, label_text)
    # render("wire_melt_500000.dump")

    # pos_property = data.particles.positions
    # l1 = []
    # for pos in pos_property:
    #     l1.append(pos[2])
    #
    # a = max(l1)
    # b = min(l1)
    # sr = (a - b) / 2
    # c = b + sr
    # print(c)

    # print(f"Длина : {(MaxX - MinX)}")
    # print(f"Высота : {(MaxY - MinY)}")
    # print(f"Ширина : {(MaxZ - MinZ)}")
    #
    # slice_mod = SliceModifier(distance=0.01, normal=(1, 0, 0))
    # pipeline.modifiers.append(slice_mod)
    # data = pipeline.compute()

    #     bar_length = 40   # Simulation units (e.g. Angstroms)
    #     bar_color = QtGui.QColor(0,0,0)
    #     label_text = f"{bar_length/10} nm"
    #     label_color = QtGui.QColor(255,255,255)
    #
    # # This function is called by OVITO on every viewport update.
    #     def render(args):
    #         if args.is_perspective:
    #             raise Exception("This overlay only works with non-perspective viewports.")
    #
    #     # Compute length of bar in screen space
    #         screen_length = args.project_size((0,0,0), bar_length)
    #
    #         # Define geometry of bar in screen space
    #         height = 0.07 * args.painter.window().height()
    #         margin = 0.02 * args.painter.window().height()
    #         rect = QtCore.QRectF(margin, margin, screen_length, height)
    #
    #         # Render bar rectangle
    #         args.painter.fillRect(rect, bar_color)
    #
    #         # Render text label
    #         font = args.painter.font()
    #         font.setPixelSize(height)
    #         args.painter.setFont(font)
    #         args.painter.setPen(QtGui.QPen(label_color))
    #         args.painter.drawText(rect, QtCore.Qt.AlignCenter, label_text)
    #
    vp = Viewport(type=Viewport.Type.Ortho)
    tripod = CoordinateTripodOverlay(size=0.05)
    vp.overlays.append(tripod)

    def render_scale_bar(args: PythonViewportOverlay.Arguments, length=5):
        if args.is_perspective:
            raise Exception("This overlay only works with non-perspective viewports.")
        u = length
        bar_length = u / 1000  # Simulation units (e.g. Angstroms)
        label_text = f"{u} mm"
        bar_color = QtGui.QColor(0, 0, 0)
        label_color = QtGui.QColor(255, 255, 255)

        screen_length = args.project_size((0, 0, 0), bar_length)
        height = 0.03 * args.painter.window().height()
        margin = 0.02 * args.painter.window().height()
        rect = QtCore.QRectF(margin, margin, screen_length, height)

        # Render bar rectangle
        args.painter.fillRect(rect, bar_color)

        font = args.painter.font()
        font.setPixelSize(height)  # height or 30
        args.painter.setFont(font)
        args.painter.setPen(QtGui.QPen(label_color))
        args.painter.drawText(rect, QtCore.Qt.AlignCenter, label_text)
        # QtGui.QPainter.DrawLine()

    vp.overlays.append(PythonViewportOverlay(function=render_scale_bar))

    dutDir = "D:\\OVITO_screen\\"
    # vp.type = Viewport.Type.Ortho
    vp.fov = 0.0074746
    vp.camera_pos = (0.0104947, -5e-05, 0.00560304)
    vp.camera_dir = (0, 1, 0)
    vp.render_image(size=(1600, 1200), filename=dutDir + "ViewSide.png", background=(1, 1, 1), frame=1)

    vp.fov = 0.00711783
    vp.camera_pos = (0.0108255, 3.11667e-05, 0)
    vp.camera_dir = (0, 0, -1)
    vp.render_image(size=(1600, 1200), filename=dutDir + "ViewTop.png", background=(1, 1, 1), frame=1)

    vp.fov = 0.00410214
    vp.camera_pos = (0.0506625, -0.000560686, 0.00497058)
    vp.camera_dir = (1, 0, 0)
    vp.render_image(size=(1600, 1200), filename=dutDir + "ViewFront.png", background=(1, 1, 1), frame=1)

    pipeline.modifiers.append(SliceModifier(distance=0, normal=(0.0, 1.0, 0.0)))
    pipeline.compute()

    vp.fov = 0.00743406
    vp.camera_pos = (0.00996866, 0, 0.00320925)
    vp.camera_dir = (0, -1, 0)
    vp.render_image(size=(1600, 1200), filename=dutDir + "ViewSlice.png", background=(1, 1, 1), frame=1)

    # Create a viewport:
    # viewport = Viewport(type=Viewport.Type.Top)
    #
    # # The user-defined function that will paint on top of rendered images:
    # def render_some_text(args: PythonViewportOverlay.Arguments):
    #     args.painter.drawText(10, 10, "Hello world")
    #
    # # Attach overlay function to viewport:
    # viewport.overlays.append(PythonViewportOverlay(function=render_some_text))

    # bar_length = 40
    # bar_color = QtGui.QColor(0, 0, 0)
    # label_text = f"{bar_length / 10} nm"
    # label_color = QtGui.QColor(255, 255, 255)
    #
    # def render(args):
    #     if args.is_perspective:
    #         raise Exception("This overlay only works with non-perspective viewports.")
    #
    #     # Compute length of bar in screen space
    #     screen_length = args.project_size((0, 0, 0), bar_length)
    #
    #     # Define geometry of bar in screen space
    #     height = 0.07 * args.painter.window().height()
    #     margin = 0.02 * args.painter.window().height()
    #     rect = QtCore.QRectF(margin, margin, screen_length, height)
    #
    #     # Render bar rectangle
    #     args.painter.fillRect(rect, bar_color)
    #
    #     # Render text label
    #     font = args.painter.font()
    #     font.setPixelSize(height)
    #     args.painter.setFont(font)
    #     args.painter.setPen(QtGui.QPen(label_color))
    #     args.painter.drawText(rect, QtCore.Qt.AlignCenter, label_text)
    # render(args=PythonViewportOverlay.Arguments)


ovitoMain1()
