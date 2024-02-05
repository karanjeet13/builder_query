from django.test import TestCase
import inspect

def load_class(reflections, annotation):
    classes = reflections.get_types_annotated_with(annotation)
    if not classes:
        fail(f"If the builder pattern is implemented, there should be a class annotated with {annotation.__name__}")
    if len(classes) > 1:
        fail(f"There should be exactly one class annotated with {annotation.__name__}")

    return classes.pop()

def load_inner_class(outer_class):
    inner_classes = outer_class.__class__.__dict__.values()
    for inner_class in inner_classes:
        if inspect.isclass(inner_class) and inspect.isfunction(inner_class) and inspect.isgeneratorfunction(inner_class):
            return inner_class

    return None

def get_reference_to_outer_class():
    inner_class_fields = inner_class.__dict__.values()
    for inner_field in inner_class_fields:
        if inspect.isfunction(inner_field) and inspect.isgeneratorfunction(inner_field) and inner_field.__annotations__.get('return') == outer_class:
            return inner_field

    return None


# Create your tests here.
